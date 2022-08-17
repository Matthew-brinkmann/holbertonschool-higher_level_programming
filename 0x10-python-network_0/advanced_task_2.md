# How I acheived task 102

## ❓Project task❓
```
Write a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

You have to use curl
You are not allow to use echo, cat, etc. to display the final result
```

## ❗Solution❗

## 1️⃣
The first clue is in the wording of the file "catch_me" which implies that there will be a number of redirects, and depending on what input was given is where the redirect would take you.
```mermaid
graph TD;
    curl-->correct_input;
    curl-->Incorrect_input;
    correct_input-->You_got_me;
    Incorrect_input-->some_error;
```
Obiously, we want to end in you_got_me.

## 2️⃣
So I decided to run the following scripts, inputting 0.0.0.0:5000/catch_me as the input.
***  
**First**: 1-body.sh - To see if we can find the end point... I got
```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
```

> This showed me that I can't run a curl normally, I'll need to use only the permitted methods.
***
**Second**: 3-methods.sh - To see what methods the URL allows... I got
```
OPTIONS, PUT
```

> This showed me that I can only use the PUT method


## 3️⃣
Now that I know i can only use the PUT method, I decided to canabalise my script 5-post_params.sh to use PUT as the command, i did this with the following.
```
curl -sLX PUT -d "test=test" 0.0.0.0:5000/catch_me 
```
To my surprise, i got the return
```
You are not user_id = 98
```
So now I knew 1 of the parameters, which allowed me to change my command.
So far, our flow chart looks like this...
```mermaid
graph TD;
    curl-->user_id=98;
    curl-->test=test;
    user_id=98-->??;
    test=test-->NOT_user_id=98;
```
SO now I could send the correct attribute:
```
curl -sLX PUT -d "user_id=98" 0.0.0.0:5000/catch_me
```
and my return was not the end, but rather
```
You are not coming from HolbertonSchool
```
Ahhh, that sucks.

## 4️⃣
So now I had to decode this clue "You are not coming from HolbertonSchool". This led me on a chase to Google.
```
GOOGLE: how to tell a HTTP request where I am coming from
```
which lead me to [this page](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin) which was the second result. The page just outlines the purpose of the **Origin** request header, which tells the server the *origin* of the request. So now, the flow chart looked like this... after a bit more reading, i realised the flow chart was looking like this...

```mermaid
graph TD;
    curl-->user_id=98;
    curl-->test=test;
    user_id=98-->origin:localHost;
    user_id=98-->origin:HolbertonSchool;
    test=test-->NOT_user_id=98;
    origin:HolbertonSchool-->??;
    origin:localHost-->NOT_from_HolbertonSchool;
```
So now, armed with the origin header, i ran,
```
curl -sLX PUT -d "user_id=98" -H "Origin:HolbertonSchool" 0.0.0.0:5000/catch_me
```
and SUCCESS!!!
```mermaid
graph TD;
    curl-->user_id=98;
    curl-->test=test;
    user_id=98-->origin:localHost;
    user_id=98-->origin:HolbertonSchool;
    test=test-->NOT_user_id=98;
    origin:HolbertonSchool-->You_Got_me!;
    origin:localHost-->NOT_from_HolbertonSchool;
```

Hope you enjoyed the process of tracing this HTTP request from the start to the end.