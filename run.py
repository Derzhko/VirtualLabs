from app import app
import argparse
import threading
outputFrame = None
lock = threading.Lock()
# initialize a flask object
if __name__ == '__main__':
    # construct the argument parser and parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=False,
                    help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=False,
                    help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
                    help="# of frames used to construct the background model")
    args = vars(ap.parse_args())
    app.run(host="0.0.0.0", port="8000", debug=True,
            threaded=True, use_reloader=False)

