#!/usr/bin/env python
# -*- coding: utf-8 -*-	

import os
from flask import Flask, request
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)
s3 = boto3.client('s3', aws_access_key_id='131604634577647851@ecstestdrive.emc.com', aws_secret_access_key='UrSsdKjfgOP3b2zoRcgTjPXEnQTH4eKFXu2m+7WY', endpoint_url='https://object.ecstestdrive.com')
public_endpoint = "https://131604634577647851.public.ecstestdrive.com/"

@app.route('/')
def WelcomePage():
    
    begin_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>ECS</title>
        <meta charset="utf-8">
        <meta name="description" content="ECS Cloud Native Application">
        <meta name="author" content="ecs1.cfapps.io">
        <meta name="keywords" content="ecs,object, storage, cloud,native,application">
        <meta name="google-signin-client_id" content="955627858473-13lq2gtfh5ep675lie2me734kf1vn538.apps.googleusercontent.com">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
        <meta http-equiv="Pragma" content="no-cache" />
        <meta http-equiv="Expires" content="0" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="apple-touch-icon" sizes="57x57" href="/static/apple-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="/static/apple-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="/static/apple-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="/static/apple-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="/static/apple-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="/static/apple-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="/static/apple-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="/static/apple-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-icon-180x180.png">
        <link rel="icon" type="image/png" sizes="192x192" href="/static/android-icon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="96x96" href="/static/favicon-96x96.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
        <link rel="manifest" href="/static/manifest.json">
        <meta name="msapplication-TileColor" content="#ffffff">
        <meta name="msapplication-TileImage" content="/static/ms-icon-144x144.png">
        <meta name="msapplication-square70x70logo" content="/static/ms-icon-70x70.png">
        <meta name="msapplication-square150x150logo" content="/static/ms-icon-150x150.png">
        <meta name="msapplication-square310x310logo" content="/static/ms-icon-310x310.png">

        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <![endif]-->


    </head>
    <body style="font-family:Roboto; background-color:SLATEGRAY" ontouchstart="">
    """

    end_html = "</body></html>"

    mid_html = """

    <style>

         html {
            height: 100%;
        }

        body {
            position: relative;
            min-height: 100%;
            -webkit-user-select: none;
            -webkit-touch-callout: none;
        }

       #g-signin2 {
            width: 100%;
        }
                
        #g-signin2 > div {
            margin: 0 auto;
        }

     
        .bottom-label {
            display: block;
            margin-left: auto;
            margin-right: auto;
            height: 45px;
            text-align: center;
            bottom: 0;
            position: absolute;
            width: 100%;
            font-weight:300;
        }
       

        .waiting-class {
            display:none;
            margin: auto;
            text-align: center;
            width:100%;
            height:100%;
            top:0;
            position:absolute;
            padding-top: 50%;
            background: rgba(0, 0, 0, 0.3)
        }

        .image-center {
            position: absolute; 
            margin: auto; 
            top: 0; 
            left: 0; 
            right: 0; 
            bottom: 0;
        }


        .google-center {
            position: absolute;
            margin: auto;
            text-align:center;
            top: calc(100% - 110px);
            left: 0; 
            right: 0; 
        }
       
    </style>

    <div class="container">

        <div style="width:100%; height:100%">
            <img src="static/ecs.png" class="image-center" style="width:192px; height:192px;">
            
            <div class="google-center">
                <div id="g-signin2"></div>
            </div>

           
        </div>

    </div>

    <div id="waiting" class="waiting-class">
        <i style="color:LIME" class="fa fa-spinner fa-pulse fa-3x fa-fw"></i>
    </div>

    <div class="bottom-class">
        <label class="bottom-label">
            <p style="color: white;">
                &copy 2019 Dell EMC.
                <br>
                <span style="color:TURQUOISE">Powered by Pivotal Cloud Foundry</span>
            </p>
        </label>
    </div>


    <script>

        function addZero(i) {
            if (i < 10) {
                i = "0" + i;
            }
            return i;
        }

        

        function onSignIn(googleUser) {

            var waiting = document.getElementById('waiting');
            waiting.style.display="block";

            var user_id = googleUser.getBasicProfile().getId();
            var folder_name = '';
            

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/HomePage/'+ user_id, true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onload = function() {
                document.open();
                document.write(xhr.responseText);
                document.close();

            };

            xhr.send('folder_name='+folder_name);

        }
        
        
        function onFailure(error) {
            console.log(error);
        }
            
        function renderButton() {
            gapi.signin2.render('g-signin2', {
                'scope': 'profile email',
                'width': 254,
                'longtitle': true,
                'theme': 'dark',
                'onsuccess': onSignIn,
                'onfailure': onFailure
            });
        }

        
    </script>

    <script src="https://apis.google.com/js/platform.js?onload=renderButton" async defer></script>

  
    """
    
    return begin_html + mid_html + end_html

@app.route('/HomePage/<user_id>', methods=['POST'])
def HomePage(user_id):
    
 
    print "HomePage:user_id:"+user_id

    folder_name = request.form['folder_name']
    
    table_padding = "220px"

    table = listFolder(user_id, folder_name)
    

    begin_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>ECS</title>
        <meta charset="utf-8">
        <meta name="description" content="ECS Cloud Native Application">
        <meta name="author" content="ecs1.cfapps.io">
        <meta name="keywords" content="ecs,object, storage, cloud,native,application">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />
        <meta http-equiv="Pragma" content="no-cache" />
        <meta http-equiv="Expires" content="0" />
        <meta name="format-detection" content="telephone=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700">

        <link rel="shortcut icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
        <link rel="apple-touch-icon" sizes="57x57" href="/static/apple-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="/static/apple-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="/static/apple-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="/static/apple-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="/static/apple-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="/static/apple-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="/static/apple-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="/static/apple-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-icon-180x180.png">
        <link rel="icon" type="image/png" sizes="192x192" href="/static/android-icon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32" href="/static/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="96x96" href="/static/favicon-96x96.png">
        <link rel="icon" type="image/png" sizes="16x16" href="/static/favicon-16x16.png">
        <link rel="manifest" href="/static/manifest.json">
        <meta name="msapplication-TileColor" content="#ffffff">
        <meta name="msapplication-TileImage" content="/static/ms-icon-144x144.png">
        <meta name="msapplication-square70x70logo" content="/static/ms-icon-70x70.png">
        <meta name="msapplication-square150x150logo" content="/static/ms-icon-150x150.png">
        <meta name="msapplication-square310x310logo" content="/static/ms-icon-310x310.png">

        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <![endif]-->
  	
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>


    </head>
    
    <body style="font-family:Roboto; background-color:SLATEGRAY" ontouchstart="">
    
    """

    end_html = "</body></html>"

    addZero = """
        function addZero(i) {
        if (i < 10) {
            i = "0" + i;
        }
        return i;
    }
    """


    signOut_function = """
    function signOut() {

        document.location.href = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=https://ecs1.cfapps.io";

    };
        """
   
  
    addFolder = """
    function addFolder(user_id, current_folder) {

        var folder_name = prompt("Folder Name", "New Folder");
        if (folder_name != null) {

            folder_name = current_folder + folder_name + '/'

            var waiting = document.getElementById('waiting');
            waiting.style.display="block";

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/AddFolder/'+ user_id, true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onload = function() {
                               
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/HomePage/'+ user_id, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

                xhr.onload = function() {
                    document.open();
                    document.write(xhr.responseText);
                    document.close();

                };

                xhr.send('folder_name='+current_folder);
                
            };

            xhr.send('folder_name='+folder_name);

        }


    };
    """

    fileUpload = """

    function fileUpload(user_id, current_folder, file_name) {
        var f = file_name.files[0];
        var waiting = document.getElementById('waiting');
        waiting.style.display="block";

        var formData = new FormData();

        formData.append('current_folder',current_folder)
        formData.append('file', f)

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/FileUpload/'+ user_id, true);
        
        xhr.onload = function() {
            
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/HomePage/'+ user_id, true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onload = function() {
                document.open();
                document.write(xhr.responseText);
                document.close();

            };

            xhr.send('folder_name='+current_folder);

        };

        xhr.send(formData);

    };
    """

    cogFunction = r"""
    function cogFunction() {
        
        alert('Email: DucThang.Nguyen@emc.com\r\n'+
                'Mobile: (+84)904994503');
        
    };
    """

    expandFolder = """
    function expandFolder(user_id, folder_name) {
        
        var waiting = document.getElementById('waiting');
        waiting.style.display="block";

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/HomePage/'+ user_id, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function() {
            document.open();
            document.write(xhr.responseText);
            document.close();

        };

        xhr.send('folder_name='+folder_name);

    };
    """

   
    shareLink = """
    function shareLink(user_id, object_name, download_link) {
        
                    
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/ShareLink/'+ user_id, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function() {
                
            var copyText = document.createElement("INPUT");
            copyText.setAttribute("type", "text");
            copyText.value = download_link;
            document.body.appendChild(copyText);  
            
            copyText.select();
            document.execCommand("copy");
            document.body.removeChild(copyText);  
    
            alert("Link Copied: " + copyText.value);        

        };

        xhr.send('file_name='+object_name);
        
    };
    """

    downloadFile = """
    function downloadFile(x,user_id, object_name, download_link) {
        
                    
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/DownloadFile/'+ user_id, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        xhr.onload = function() {

            window.open(download_link);

        };

        xhr.send('file_name='+object_name+'&ACL=public-read');
        
    };
    """

    deleteFile = """
    function deleteFile(user_id, current_folder, file_name) {
        
        if (confirm("Are you sure to delete this file ?")) {

            var waiting = document.getElementById('waiting');
            waiting.style.display="block";
            
            var object_name = current_folder + file_name;

            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/DeleteFile/'+ user_id, true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onload = function() {
                
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/HomePage/'+ user_id, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

                xhr.onload = function() {
                    document.open();
                    document.write(xhr.responseText);
                    document.close();

                };

                xhr.send('folder_name='+current_folder);

            };

            xhr.send('file_name='+object_name);

        }
        

    };
    """


    deleteFolder = """
    function deleteFolder(user_id, current_folder, folder_name) {
        
     
        if (confirm("Are you sure to delete this folder ?")) {

            var waiting = document.getElementById('waiting');
            waiting.style.display="block";
            
            var xhr = new XMLHttpRequest();
            xhr.open('POST', '/DeleteFolder/'+ user_id + '/108761518397694192075', true);
            xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

            xhr.onload = function() {
                
                var xhr = new XMLHttpRequest();
                xhr.open('POST', '/HomePage/'+ user_id, true);
                xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

                xhr.onload = function() {
                    document.open();
                    document.write(xhr.responseText);
                    document.close();

                };

                xhr.send('folder_name='+current_folder);

            };

            xhr.send('folder_name='+folder_name);
        }
        
    };
    """


    six_jars_style = """

        html {
            height: 100%;
        }

        body {
            position: relative;
            padding-bottom: 4em;
            min-height: 100%;
            -webkit-user-select: none;
            -webkit-touch-callout: none;
        }

        table {
            width: 100%;
        }

        td {
            border-bottom: 1px solid DARKSLATEGRAY;
            padding-top:10px;
            padding-bottom:10px;

        }

        input[type="button"] {
            display: none;
        }
        
        .sixjars-label-class {
            border: 1px solid DARKSLATEGRAY;
            color: LIGHTGRAY;
            display: block;
            cursor: pointer;
            padding: 6px 0px;
            width: 100%;
            height: 35px;
            font-weight:400;
        }

        .sixjars-label-class:active {
            color: DARKSLATEGRAY;
            border: 1px solid LIGHTGRAY;
        }

        .balance-label-class {
            background-color: DARKSLATEGRAY;
            border: 1px solid DARKSLATEGRAY;
            color: LIGHTGRAY;
            display: block;
            padding: 6px 0px;
            width: 100%;
            height: 100px;
        }


        .income-expense-label {
            background-color: DARKSLATEGRAY;
            border: 1px solid DARKSLATEGRAY;
            color: LIGHTGRAY;
            display: block;
            padding: 6px 0px;
            width: 100%;
            height: 70px;

        }

        
        .menu-label {
            background-color: DARKSLATEGRAY;
            border: 1px solid DARKSLATEGRAY;
            color: LIGHTGRAY;
            display: block;
            padding: 10px 0px;
            width: 100%;
            height: 50px;
            text-align: center;
        }


        .bottom-label {
            display: block;
            margin-left: auto;
            margin-right: auto;
            height: 45px;
            text-align: center;
            bottom: 0;
            position: absolute;
            width: 100%;
            font-weight:300;
        }

       
        .minus-button-label {
            color: TURQUOISE;
            cursor: pointer;
            display: block;
            text-align: center;
        }


        .minus-button-label:active {
            color: LIGHTGRAY;
        }

        .menu-button-label {
            display: block;
            color: LIGHTGRAY;
            cursor: pointer;
        }

        
        .menu-button-label:active {
            color: TURQUOISE;
        }
        
        .waiting-class {
            display:none;
            margin: auto;
            text-align: center;
            width:100%;
            height:100%;
            top:0;
            padding-top: 50%;
            position:absolute;
            background: rgba(0, 0, 0, 0.3)
        }

        .progress-class {
            background-color:LIGHTGRAY;
            height:2px;
            width:100px;
        }


        /* The container <div> - needed to position the dropdown content */
        .dropdown {
            position: relative;
            display: inline-block;
        }

        /* Dropdown Content (Hidden by Default) */
        .dropdown-content {
            display: none;
            position: absolute;
            left: -100px;
            background-color: #f1f1f1;
            min-width: 100px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }

        /* Links inside the dropdown */
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }

        /* Change color of dropdown links on hover */
        .dropdown-content a:hover {background-color: #ddd;}

        /* Show the dropdown menu on hover */
        .dropdown:hover .dropdown-content {display: block;}

    """


    mid_html = """
    
    <style>
        /*------ six jars style ---------*/
        {six_jars_style}
    </style>


    <div class="container">

        <div class="col-sx-12" style="background-color:DARKSLATEGRAY">
    	    <h4>
                <p class="text-center" style="color:white;">Objects</p>
            </h4>
        </div>
  
        <div style="height:calc(100vh - {table_padding}); min-height:calc(630px - {table_padding}); overflow:auto; -webkit-overflow-scrolling: touch">
            {table}
        </div>
        
        <div class="menu-class">
            <label class="menu-label">
                <div class="col-xs-3">
                    <input id="home-submit" type="button">
                    <label for="home-submit" class="menu-button-label">
                        <i class="fas fa-home fa-2x" style="color:TURQUOISE"></i>
                    </label>
                </div>
                <div class="col-xs-3">
                    <input id="history-submit" type="button" onclick="addFolder('{user_id}','{current_folder}')">
                    <label for="history-submit" class="menu-button-label">
                        <i class="fas fa-folder-plus fa-2x"></i>
                    </label>
                </div>
                <div class="col-xs-3">
                    <label class="menu-button-label">
                        <i class="fas fa-file-upload fa-2x"></i>
                        <input type="file" style="display: none;" id="file" name="file" onchange="fileUpload('{user_id}','{current_folder}',this)">
                    </label>
                </div>
                <div class="col-xs-3">
                    <input id="cog-submit" type="button" onclick="cogFunction()">
                    <label for="cog-submit" class="menu-button-label">
                        <i class="fas fa-info-circle fa-2x"></i>
                    </label>
                </div>
            </label>

        </div>
	
        <script>
            {addZero}
            {signOut_function}
            {addFolder}
            {fileUpload}
            {cogFunction}
            {expandFolder}
            {deleteFile}
            {shareLink}
            {deleteFolder}
            {downloadFile}

        </script>

        <div id="fb-root"></div>
        <script async defer src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.2&appId=392841268177993&autoLogAppEvents=1"></script>
       
    </div>


    <div id="waiting" class="waiting-class">
        <i style="color:LIME" class="fa fa-spinner fa-pulse fa-3x fa-fw"></i>
    </div>

    <div class="bottom-class">
        <label class="bottom-label">
            <p style="color: white;">
                Signed in as {user_id}
                <br> <a href="javascript:void(0)" onclick="signOut();" style="color:TURQUOISE">Sign out</a>
            </p>
        </label>
    </div>
   
    """.format(signOut_function=signOut_function,
                table=table,
                six_jars_style=six_jars_style,
                addZero=addZero,
                addFolder=addFolder,
                fileUpload=fileUpload,
                cogFunction=cogFunction,
                user_id=user_id,
                table_padding=table_padding,
                expandFolder=expandFolder,
                deleteFile=deleteFile,
                current_folder=folder_name,
                shareLink=shareLink,
                deleteFolder=deleteFolder,
                downloadFile=downloadFile)
    
    return begin_html + mid_html + end_html

def listFolder(user_id, folder_name):
    
    try:
        objs = s3.list_objects_v2(Bucket=user_id,Delimiter='/', Prefix=folder_name)
    except ClientError as e:
        if e.response['Error']['Code'] == 'NoSuchBucket':
            s3.create_bucket(Bucket=user_id)
            return listFolder(user_id, '')


    folder_name2 = folder_name[:-1]
    i = folder_name2.rfind('/')
    parent_folder = folder_name2[:i+1]
    

    print 'listFolder:current_folder:'+folder_name
    print 'listFolder:parent_folder:'+parent_folder

    table_begin = """
        <table>
    """
    table_end = """
        </table>
    """

    table_body = ""

    #add back folder
    if len(folder_name) > 0:
        table_body = table_body + """
            <tr style="cursor:pointer;">
                <td id="cel1" style="width:40px;  color:TURQUOISE"><i class="far fa-folder fa-2x"></i></td>
                <td id="cel2" onclick="expandFolder('{user_id}','{parent_folder}')">
                    <span style="color:white; text-align:left;">...</span>
                </td>
                <td id="cel3" style="text-align:center; color:white">
                </td>
            </tr>
        """.format(parent_folder=parent_folder,
                    user_id=user_id)


    #list folder
    if 'CommonPrefixes' in objs:
        for obj in objs['CommonPrefixes']:
            object_name = obj['Prefix'][len(folder_name):]
            folderName = folder_name+object_name

            table_body = table_body + """
                <tr style="cursor:pointer;">
                    <td id="cel1" style="width:40px;  color:TURQUOISE"><i class="far fa-folder fa-2x"></i></td>
                    <td id="cel2" onclick="expandFolder('{user_id}','{folderName}')">
                        <span style="color:white; text-align:left;">{object_name}</span>
                    </td>
                    <td id="cel3" style="text-align:center; color:white" onclick="deleteFolder('{user_id}','{current_folder}','{folderName}')">
                        <i class="fas fa-trash-alt"></i>
                    </td>
                </tr>
            """.format(object_name=object_name,
                        folderName=folderName,
                        user_id=user_id,
                        current_folder=folder_name)

    #list files
    if 'Contents' in objs:
        for obj in objs['Contents']:
            if (obj['Key'] == folder_name):
                continue
            
            file_name = obj['Key'][len(folder_name):]
            file_date = obj['LastModified'].date()
            file_size = str(obj['Size']/1024) + 'KB'

            download_link = public_endpoint + user_id + '/' + folder_name+file_name

            object_head = s3.head_object(Bucket=user_id, Key=obj['Key'])
            object_name = obj['Key']

            file_icon = """<i class="far fa-file fa-2x"></i>"""

            if 'wordprocessingml' in object_head['ContentType']:
                file_icon = """<i style="color:DEEPSKYBLUE" class="far fa-file-word fa-2x"></i>"""

            if 'spreadsheetml' in object_head['ContentType']:
                file_icon = """<i style="color:LIMEGREEN" class="far fa-file-excel fa-2x"></i>"""

            if 'presentationml' in object_head['ContentType']:
                file_icon = """<i style="color:ORANGERED" class="far fa-file-powerpoint fa-2x"></i>"""

            if 'image' in object_head['ContentType']:
                file_icon = """<i style="color:GOLD" class="far fa-file-image fa-2x"></i>"""

            if 'audio' in object_head['ContentType']:
                file_icon = """<i style="color:AQUA" class="far fa-file-audio fa-2x"></i>"""

            if 'video' in object_head['ContentType']:
                file_icon = """<i style="color:HOTPINK" class="far fa-file-video fa-2x"></i>"""

            if 'text' in object_head['ContentType']:
                file_icon = """<i class="far fa-file-alt fa-2x"></i>"""

            if 'pdf' in object_head['ContentType']:
                file_icon = """<i style="color:CRIMSON" class="far fa-file-pdf fa-2x"></i>"""
            
            table_body = table_body + """
                <tr style="cursor:pointer;">
                    <td id="cel1" style="width:40px; color:white">{file_icon}</td>
                    <td id="cel2">
                        <span style="color:white">{file_name}</span><br>
                        <span style="font-size:small; font-weight:300; color:LIGHTGRAY">{file_date} - </span>
                        <span style="font-size:small; font-weight:300; color:LIGHTGRAY">{file_size}</span>
                    </td>
                    <td id="cel3" style="text-align:center; color:white">
                        <div class="dropdown">
                            <i class="fas fa-ellipsis-v"></i>
                            <div style="text-align:left" class="dropdown-content">
                                <a onclick="downloadFile(this,'{user_id}','{object_name}','{download_link}')" target="_blank" download><i class="fas fa-download"></i> Save</a>
                                <a onclick="shareLink('{user_id}','{object_name}','{download_link}')"><i class="fas fa-share-alt-square"></i> Share</a>
                                <a onclick="deleteFile('{user_id}','{current_folder}','{file_name}')"><i class="fas fa-trash-alt"></i> Delete</a>
                            </div>
                        </div>
                    </td>                   
                </tr>
            """.format(file_name=file_name,
                        file_date=file_date,
                        file_size=file_size,
                        file_icon=file_icon,
                        user_id=user_id,
                        current_folder=folder_name,
                        download_link=download_link,
                        object_name=object_name)

    return table_begin + table_body + table_end

@app.route('/AddFolder/<user_id>', methods=['POST'])
def AddFolder(user_id):
    
    folder_name = request.form['folder_name']

    print "AddFolder:folder_name:"+folder_name

    s3.put_object(Bucket=user_id, Key=folder_name)
    
    return ""

@app.route('/FileUpload/<user_id>', methods=['POST'])
def FileUpload(user_id):
    
  
    current_folder = request.form['current_folder']
    f = request.files['file']
    file_name = f.filename
    content_type = f.content_type

    print "FileUpload:user_id:"+user_id
    print "FileUpload:current_folder:"+current_folder
    print "FileUpload:file_name:"+file_name
    print "FileUpload:content_type:" + content_type

    s3.put_object(Bucket=user_id, Key=current_folder+file_name, Body=f.read(), ContentType=content_type)
    
    return ""

@app.route('/DeleteFile/<user_id>', methods=['POST'])
def DeleteFile(user_id):
    
    file_name = request.form['file_name']

    print "DeleteFile:file_name:"+file_name

    s3.delete_object(Bucket=user_id, Key=file_name)
    
    return ""

@app.route('/DeleteFolder/<user_id>/<folder_name>', methods=['POST'])
def DeleteFolder(user_id, folder_name):
    
    if folder_name == "108761518397694192075":
        folder_name = request.form['folder_name']

    print "DeleteFolder:folder_name:"+folder_name

    objects_to_delete = []

    object_list = s3.list_objects_v2(Bucket=user_id,Delimiter='/', Prefix=folder_name)

    if 'CommonPrefixes' in object_list:
        for obj in object_list['CommonPrefixes']:
            objects_to_delete.append({'Key':obj['Prefix']})
            DeleteFolder(user_id, obj['Prefix'])

    if 'Contents' in object_list:
        for obj in object_list['Contents']:
            objects_to_delete.append({'Key':obj['Key']})
    
    s3.delete_objects(Bucket=user_id, Delete={'Objects': objects_to_delete})


    return ""

@app.route('/ShareLink/<user_id>', methods=['POST'])
def ShareLink(user_id):
    
    file_name = request.form['file_name']

    print "ShareLink:file_name:"+file_name

    s3.put_object_acl(Bucket=user_id, Key=file_name, ACL='public-read')

    return ""

@app.route('/DownloadFile/<user_id>', methods=['POST'])
def DownloadFile(user_id):
    
    file_name = request.form['file_name']
    acl = request.form['ACL']

    print "DownloadFile:file_name:"+file_name
    print "DownloadFile:acl:"+acl

    s3.put_object_acl(Bucket=user_id, Key=file_name, ACL=acl)

    return ""


if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=int(os.getenv('PORT', '5000')))