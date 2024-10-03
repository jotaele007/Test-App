import frida, sys, time

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

js = """Java.perform(function() {
    var textViewClass = Java.use("android.widget.TextView");
  
    textViewClass.setText.overload("java.lang.CharSequence").implementation = function(x) {
        var string = Java.use('java.lang.String');
        return this.setText(string.$new("This text is currently being hooked"));
    }
});"""

device = frida.get_usb_device()
pid = device.spawn(["com.ds.testapp"])
session = device.attach(pid)
script = session.create_script(js)
script.on('message', on_message)
script.load()
device.resume(pid)
sys.stdin.read()
