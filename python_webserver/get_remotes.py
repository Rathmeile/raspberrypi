#https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/

from flask import Flask, request
app = Flask(__name__)

in_memory_datastore = {
    "Samsung TV": {"brand":"Samsung","model":"st100","filename":"samsunsg_st100"}
}


@app.route('/remote/<brand>')
def get_remote_brand(brand):
    return in_memory_datastore[brand]

@app.get('/remote')
def list_remote_drivers():
    brand_filter = request.args.get('brand') or ''
    qualifying_data = list (
        filter(
            lambda pl: pl['brand'].lower() == brand_filter,
            in_memory_datastore.values()
        )
    )

    return {"data", qualifying_data}


def list_remote_drivers():
    return ['1','2']

def add_remote_driver(brand, model):
    in_memory_Datastore[]
    return True

@app.route('/remote+drivers', methods=['GET', 'POST'])
def programming_languages_route():
   if request.method == 'GET':
       return list_remote_drivers()
   elif request.method == "POST":
       return add_remote_driver(request.get_json(force=True))
