from flask import Flask, request
import requests
import redis

app = Flask(__name__)

def get_redis_client():
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses = True)

rd = get_redis_client()
keys_r = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/tsv/hgnc_complete_set.txt')
keys_list = keys_r.text.split('\n')[0].split('\t')

@app.route('/data', methods=['POST','GET','DELETE'])
def handle_data() -> list:
    """
    If methods is POST, loads the HGNC data set into redis and returns message
    If method is GET, returns data from redis
    If method is DELETE, clears the data in redis and returns message

    Args:
        no arguments

    Returns:
        hgnc_data (list): (if method is GET) list of dictionaries of the gene data in redis
    """
    if request.method == 'POST':
        response = requests.get('https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        for item in response.json()['response']['docs']:
            rd.hset(item['hgnc_id'], mapping = item)
        return 'HGNC data is loaded into Redis\n'
    elif request.method == 'GET':
        hgnc_data = []
        for key in rd.keys():
            hgnc_data.append(rd.hgetall(key))
        return hgnc_data
    elif request.method == 'DELETE':
        rd.flushdb()
        return 'HGNC data has been deleted from Redis\n'
    else:
        return 'The method you tried does not work\n'

@app.route('/genes', methods=['GET'])
def get_genes() -> list:
    """
    Returns a list of the genes currently in redis for the HGNC database for the '/genes' route
    
    Args:
        no arguments
    
    Returns:
        genes_list (list): list of strings of the hgnc_ids
    """
    genes_list = []
    genes_list = rd.keys()
    return genes_list

@app.route('/genes/<hgnc_id>', methods=['GET'])
def get_gene_info(hgnc_id: str) -> dict:
    """
    Returns a dictionary with information about the specific gene if found in the HGNC database for the '/genes/<hgnc_id>' route

    Args:
        hgnc_id (str): the HGNC ID for the gene

    Returns:
        gene_info (dict): dictionary with information about the specified gene, if gene not found, will be empty dict
    """
    gene_info = {}
    if hgnc_id in rd.keys():
        gene_info = rd.hgetall(hgnc_id)
        for key in keys_list:
            if key not in gene_info:
                gene_info[key] = ""
    return gene_info

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
