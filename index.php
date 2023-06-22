<!DOCTYPE html>
<html>
  <head>
    <title>Login Page</title>
    <link rel="stylesheet" type="text/css" href="index.css" />
  </head>
  <body>
    <div class="container">
      <img src="src/css/external/logo.png">
      <form action="login.py" method="post">
        <div class="form-group">
          <label for="email">Email<br></label>
          <input
            type="text"
            class="form-control"
            id="email"
            name="email"
          />
        </div>
        <div class="form-group">
          <label for="password">Password<br></label>
          <input
            type="password"
            class="form-control"
            id="password"
            name="password"
          />
        </div><br>
        <input type="submit" class="btn btn-primary" value="LOGIN"/>
        <a class="reg" href="registrasi.php">
          <div>Create an account here!</div>
        </a>
      </form>
    </div>
  </body>
</html>
