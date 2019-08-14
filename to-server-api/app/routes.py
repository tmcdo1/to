from flask import redirect, request, jsonify, make_response
import app.utils as utils
from app import app, models, db

# TODO: secure the flask app: Securing Flask web applications - Alexey Smirnov - Medium

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the API'

@app.route('/create-alias', methods=['POST'])
@utils.validate_host
def create_alias():
    # Get the alias and target from request
    req_data = {}
    if request.is_json:
        req_data = request.get_json()
    else:
        res_data = {
            'message': 'Not a valid request type'
        }
        return make_response(jsonify(res_data), 500)

    try:
        new_alias = models.Alias(alias=req_data['alias'], target=req_data['target'])
        db.session.add(new_alias)
        db.session.commit()
    except:
        res_data = {
            'message': 'Error creating alias'
        }
        return make_response(jsonify(res_data), 500)

@app.route('/alias/<string:alias>', methods=['GET'])
@utils.validate_host
def get_target(alias):
    result = models.Alias.query.filter_by(alias=alias).first()
    if result == None:
        res_data = {
            'message': f'Could not find the alias: {alias}'
        }
        return make_response(jsonify(res_data), 404)
    else:
        res_data = {
            'alias': result.alias,
            'target': result.target
        }
        return make_response(jsonify(res_data), 200)

@app.route('/search', methods=['GET'])
@utils.validate_host
def search_alias():
    # TODO: Use elasticsearch for getting best matches
    query = request.args.get('query')
    aliases = models.Alias.query.filter(models.Alias.alias.contains(query)).limit(10).all()
    res_data = {
        'aliases': aliases
    }
    return make_response(jsonify(res_data), 200)