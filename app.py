from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/command', methods=['GET'])
def command():
    act = request.args.get('act')
    print(f"Received action: {act}")
    
    # 你可以在這裡加入傳送給 ESP32 的邏輯
    if act == 'turn_on':
        message = 'Device turned ON'
    elif act == 'turn_off':
        message = 'Device turned OFF'
    else:
        message = 'Unknown command'

    return jsonify({'result': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
