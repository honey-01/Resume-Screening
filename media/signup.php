<?php
include("header.php");
?>

  <!-- ======= Hero Section ======= -->
<br><br><br><br>

  <main id="main" style="min-height:640px;">

   
    <section id="contact" class="contact">
      <div class="container">

        <div class="section-title" data-aos="fade-up">
          <h2>Sign In</h2>
        </div>

        <div class="row justify-content-center">

          <div class="col-lg-5 col-md-12" data-aos="fade-up" data-aos-delay="300">
            <form method="POST"  enctype="multipart/form-data" class="php-email-form">
              
			  <div class="form-group mt-3">
			    <label for="name">Name</label>
			    <input type="text" class="form-control" name="name"  placeholder="Name" required autocomplete="off">
			  </div>
			  <div class="form-group mt-3">
			    <label for="name">Email</label>
			    <input type="email" class="form-control" name="email"  placeholder="Email" required autocomplete="off">
			  </div>
              <div class="form-group mt-3">
                <label for="name">Password</label>
                <input type="password" class="form-control" name="password"  placeholder="Password" required autocomplete="off">
              </div>
              <div class="text-center"><button type="submit" name="submit">Sign Up</button></div> <br>
              <div class="text-center">Already have an account? <a href="signin.php">Sign In</a></div>
            </form>
          </div>

        </div>
<?php
include ("connection.php");
if(isset($_POST['submit']))
{
    $name=$_POST['name'];
	$email=$_POST['email'];
	$pwd=$_POST['password'];
 
    $ins="insert into reg(name,email,password) values('$name','$email','$pwd')";
    if(mysqli_query($con,$ins))
	{
	echo '<script>alert("Succesfully Registered!")
window.location="signin.php"	
</script>'; 
	
}
}
?>

      </div>
    </section><!-- End Contact Section -->

  </main><!-- End #main -->

  <!-- ======= Footer ======= -->
  

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/purecounter/purecounter.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Template Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html>