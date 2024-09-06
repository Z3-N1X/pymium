base_html = """{$using pymium}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{$title}</title>
    <script src="qrc:///qtwebchannel/qwebchannel.js"></script>
    </script>
    <script language="JavaScript">
        function sendtopy(text) {  
        new QWebChannel(qt.webChannelTransport, function (channel) {
          window.handler = channel.objects.handler;
          
          handler.test1(text)
        })};
    </script>
</head>
{$space}
</html>"""