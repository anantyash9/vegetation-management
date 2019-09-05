#!/usr/bin/env python
from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import dist_updater
import cv2
import images
from reset import reset
from vegetationPostgres.vegetation import Vegetation
from datetime import date

app = Flask(__name__)
CORS(app)

@app.route('/reset_graph')
def reset_graph():
    dist_updater.reset_globals()
    return Response('done')

@app.route('/graph')
def graph():
    response={}
    response['data'] = dist_updater.json
    response['safety']=0.2
    return jsonify(response)

@app.route('/startscan')
def scanstart():
    reset()
    dist_updater.reset_globals()
    return Response('scan started')

@app.route('/stopscan')
def scanstop():
    veg=Vegetation()
    veg.pushData('waka',date(2019,10,10),'adasdas',graph_data=dist_updater.json, point_cloud=images.point)
    return Response('scan stopped')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005, debug=True)