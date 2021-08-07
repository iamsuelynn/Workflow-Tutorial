from flask import Flask, request, make_response, jsonify
import pandas as pd
import gcsfs
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq
import os

app = Flask(__name__)

app.config["DEBUG"] = True #If the code is malformed, there will be an error shown when visit app

@app.route("/state/<state>", methods=["GET"])
def retrieve_table(state):
    
    client = bigquery.Client()
    table_id = 'Books.books_title_author'
    sql = "SELECT * FROM `sue-gcp-learning-env.public_data.covid19_tracking_cases_by_state` where state ='"+state+"'"

    state_cases = client.query(sql).to_dataframe()
    
    state = state_cases.state[0]
    Total_Cases = state_cases.Total_cases[0]
    
    
    return {"State":state ,"Total":Total_Cases}
