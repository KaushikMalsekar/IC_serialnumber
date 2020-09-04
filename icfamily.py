from flask import Flask, jsonify, abort

app = Flask(__name__)

icsns = [
    {
        'no':1,
        'title': u'7401',
        'description': u'quad 2-input NAND gate',
        'output-pins': u'open-collector-14'

    },
    {
        'no':2,
        'title': u'7402',
        'description': u'quad 2-input NOR gate',
        'output-pins': u'--14'
    },
     {
        'no':8,
        'title': u'7408',
        'description': u'quad 2-input AND gate',
        'output-pins': u'--14'
            },
      {
        'no':3,
        'title': u'7403',
        'description': u'quad 2-input NOR gate',
        'output-pins': u'--14'
    },
       {
        'no':5,
        'title': u'7405',
        'description': u'hex inverter gate',
        'output-pins': u'open collector-14'
    },
        {
        'no':4,
        'title': u'7404',
        'description': u'hex inverter gate',
        'output-pins': u'open collector-14'
    },
             {
        'no':6,
        'title': u'7406',
        'description': u'hex inverter gate',
        'output-pins': u'open collector 30v/40ma-14'
    },
         {
        'no':8,
        'title': u'7408',
        'description': u'quad 2-input AND gate',
        'output-pins': u'open collector 30v/40ma-14'
    }
]

@app.route('/icnumber/<int:ic_no>', methods=['GET'])
def get_icsn(ic_no):
    icsn= [icsn for icsn in icsns if icsn['no'] == ic_no]
    if len(icsn) == 0:
        abort(404)
    return jsonify({'icsn': icsn[0]})

if __name__ == '__main__':
    app.run(debug=True)


