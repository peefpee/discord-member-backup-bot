from flask import Flask,request,render_template,redirect,url_for
import requests
app = Flask(__name__)
app.debug = True
import os,json
config =json.load(open('config.json'))
users = json.load(open('users.json'))
def saveusers():
    with open('users.json','w') as f:
        json.dump(users,f)
clientid = config["clientid"]
clientsecret = config["clientsecret"]
redirecturl=config["redirecturl"]
guildid = config["guildid"]
bottoken = config["bottoken"]
sitekey=config["sitekey"]



API_ENDPOINT = 'https://discord.com/api/v10'

        
def exchange_code(code):
  data = {
    'client_id':clientid,
    'client_secret': clientsecret,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirecturl
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  return r.json()
def add_to_guild(accesscode,refresh_token):

        r = requests.get('https://discord.com/api/v10/oauth2/@me',headers={"Authorization" : f'Bearer {accesscode}',})
        userid=r.json()["user"]["id"]
        url = f"{API_ENDPOINT}/guilds/{guildid}/members/{userid}"

        headers = {
                "Authorization" : f"Bot {bottoken}",
            }

        payload = {
                'access_token' : f"{accesscode}"
            }
        response = requests.put(url=url, json=payload, headers=headers)




authed = '''<!DOCTYPE html>
<html lang="en">
<meta name="hilltopads-site-verification" content="8d5e2fbe59a1f736081848b56d5dec4772d484e3" />
<head>
<title>Gay Auth</title>
<link rel="icon" href="https://techyhost.com/wp-content/uploads/2021/06/Discord-logo.png">
<meta name="description" content="Auth">
<meta charset="UTF-8">
<meta http-equiv="content-type">

<style>

body {
  font-family: "Lucida Sans";
  margin: 0;
  overflow-y: hidden;
}

@import "susy";
@import "compass/reset";

.stars, .twinkling, .clouds {
	position:absolute;
	display:block;
	top:0; bottom:0;
	left:0; right:0;
	width:100%; height:100%;
}

.stars {
	z-index: 0;
	background: #000 url('https://image.ibb.co/mjnygo/stars.png') repeat top center;
}

.twinkling{
	z-index: 1;
	background:transparent url('https://image.ibb.co/ir1DE8/twinkling.png') repeat top center;
	animation: move-twink-back 200s linear infinite;
}

.clouds{
	z-index: 2;
    background:transparent url('https://image.ibb.co/bT4N7T/clouds.png') repeat top center;
	animation: move-clouds-back 200s linear infinite;
}

@keyframes move-twink-back {
	from {background-position:0 0;}
	to {background-position:-10000px 5000px;}
}

@keyframes move-clouds-back {
	from {background-position:0 0;}
	to {background-position:10000px 0;}
}



.container {
  width: 375px;
  height: 275px;
  text-align: center;
  color: white;
  border-radius: 20%;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);

}

h2 {
  position: relative;
  bottom: 35px;
  font-size: 15px;
}

.img1 {
  position: relative;
  width: 400px;
  height: 400px;
  bottom: 125px;
  background-color: transparent;
}

footer {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 100px;
  color: white;
  font-size: 15px;
  margin-left: 20px;
}


</style>
</head>


<body>
<!-- This background is not mine! -->
<b class="stars" />
<b class="twinkling" />
<b class="clouds" />
<!-- Codepen: https://codepen.io/NazarTheVis/pen/zqXMqP -->
<!-- 2016 by Nazar The Vis Azhar -->



<div class="container">
<br />
<h1 style="font-size:35px;">Successfully Verified</h1>
<br />
<h2>You can now close this window,check for the new server</h2>

</div>

<footer>
<div>By pfp<br />
</footer>

</body>
</html>'''

indexhtml = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Discord Verify Made by Pfp :></title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  <style>
    .navbar {
      margin-bottom: 0;
      border-radius: 0;
    }
    .row.content {height: 450px}
    
    .sidenav {
      padding-top: 20px;
      background-color: #f1f1f1;
      height: 100%;
    }
    
    footer {
      background-color: #100;
      color: white;
      padding: 10px;
    }
    
    @media screen and (max-width: 767px) {
      .sidenav {
        height: auto;
        padding: 15px;
      }
      .row.content {height:auto;} 
    }
  </style>
</head>
<body>

<nav class="navbar navbar-inverse">
  <div class="container-fluid">
    <div class="navbar-header">
    </div>
    <div class="collapse navbar-collapse" id="myNavbar"> 
      <ul class="nav navbar-nav">
      <img src="https://i.imgur.com/9NLQgH0.gif">
      <img src="https://i.imgur.com/9NLQgH0.gif">
      
      </ul>
    </div>
  </div>
</nav>
  
<div class="container-fluid text-center">    
  <div class="row content">
    <div class="col-sm-2 sidenav">
      <p><a href="https://cracked.io/pfp">Cracked.io</a></p>
    </div>
    <div class="col-sm-8 text-left"> 
      <h1>Verify To Continue</h1>
      <script src="https://js.hcaptcha.com/1/api.js" async defer></script>    
      <form method="post" action="/submit" id="form1">
      <div class="h-captcha" data-sitekey="'''+sitekey+'''"></div>
      </form>

      <button type="submit" form="form1" value="Submit">Submit</button>

      <img src="#">

      <hr>

    </div>
    <div class="col-sm-2 sidenav">
      <div class="well">
      	<p>ads</p>
      </div>
      <div class="well">
        <p>ADS</p>
      </div>
    </div>
  </div>
</div>

<footer class="container-fluid text-center">
  <p>Made by Cracked.io/pfp with love ❤️</p>
</footer>
</body>
</html>
'''
@app.route('/')
def index():
     return indexhtml
@app.route('/submit',methods=["POST"])
def submit():
    captcharesponse = request.form.get('g-recaptcha-response')
    r = requests.post('https://hcaptcha.com/siteverify',data={'secret':'0x23C6e1B67919784B7C75e57c117292DE72825130','response':captcharesponse})
    if r.json()['success'] == True:
        return redirect('https://discord.com/oauth2/authorize?client_id=1053813433117716650&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fverify&response_type=code&scope=identify%20guilds.join')
    else:
        return url_for('index')



@app.route('/verify')
def verify():
    y= request.args.get('code')
    exchange = exchange_code(y)
    accesscode=exchange['access_token']
    refreshtoken= exchange['refresh_token']


    verify = f'''
      <script src="https://js.hcaptcha.com/1/api.js" async defer></script>    
      <form method="post" action="/finish">
      <div class="h-captcha" data-sitekey="{sitekey}"></div>
      <p>Verify to continue</p>
      <input type="hidden" id="accesscode" name="accesscode" value="{accesscode}">
      <input type="hidden" id="refreshtoken" name="refreshtoken" value="{refreshtoken}">
      <input type="submit" value="Submit">
      </form>
      
  '''
    return verify
@app.route('/finish',methods=["POST"])
def finish():
  captcharesponse = request.form.get('g-recaptcha-response')
  r = requests.post('https://hcaptcha.com/siteverify',data={'secret':'0x23C6e1B67919784B7C75e57c117292DE72825130','response':captcharesponse})
  if r.json()['success'] == True:
  

    accesscode = request.form.get('accesscode')
    refreshtoken = request.form.get('refreshtoken')
    r = requests.get('https://discord.com/api/v10/oauth2/@me',headers={"Authorization" : f'Bearer {accesscode}',})
    userjson = r.json()["user"]
    userid=r.json()["user"]["id"]
    
          
    if str(userid) in users:
      pass
    else:
      users[str(userid)] = userjson
      saveusers()
          


    add_to_guild(accesscode,refreshtoken)
    return authed
  else:
        return 'Captcha Error,Please redo'










if __name__ == '__main__':
    app.run()