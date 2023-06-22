<!DOCTYPE html>
<html>
  <head>
    <title>Registration Page</title>
    <link rel="stylesheet" type="text/css" href="registrasi.css" />
  </head>
  <body>
    <div class="container">
      <img src="src/css/external/logo.png">
      <form action="registrasi.py" method="post">
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
        </div>
        <div class="form-group">
          <label for="number">Phone Number<br></label>
          <input
            type="text"
            class="form-control"
            id="noTelp"
            name="noTelp"
          />
        </div><br>
        <input type="submit" class="btn btn-primary" value="SIGNUP"/>
        <a class="reg" href="index.php"><div>Back to login page</div></a>
      </form>

    </div>
  </body>
</html>