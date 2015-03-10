from flask import Flask, url_for, json, Response
app = Flask(__name__)

import Hamlib
import socket


# ----------------------------------------------------------------------------------
# Read Position

@app.route('/get_position')
def api_root():
    
    rotor = Hamlib.Rot(Hamlib.ROT_MODEL_GS232A)
    rotor.set_conf("rot_pathname","/dev/rotor_control")
    rotor.set_conf("retry","5")
    rotor.set_conf("serial_speed", "115200")
    
    rotor.open();
    
    if (rotor.error_status < 0):
        data = {
            'message'   : "Could not open connection to hamlib"
        }
        js = json.dumps(data)
    
        resp = Response(js, status=503, mimetype='application/json')
        resp.headers['Access-Control-Allow-Origin'] = '*';
        resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';
    else:
        
        elevation, azimuth = rotor.get_position()
           
        if rotor.error_status < 0:
            data = {
                'message'   : "Could not receive position"
            }
            js = json.dumps(data)
        
            resp = Response(js, status=503, mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*';
            resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';
        else:
            data = {
                'azimuth'   : int(elevation),
                'elevation' : int(azimuth)
            }
            js = json.dumps(data)
        
            resp = Response(js, status=200, mimetype='application/json')
            resp.headers['Access-Control-Allow-Origin'] = '*';
            resp.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept';


    print "\n\n"

    rotor.close()
    return resp


# ----------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)

