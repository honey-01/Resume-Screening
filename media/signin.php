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
		<?php
			error_reporting(0);
			if($_REQUEST['st']=="fail")
			{
				echo"<center><div class='alert alert-danger col-lg-5 col-md-12 fade show' role='alert'>
				<center><b>Incorrect Username or Password!<b></center>
			</div></center>";
			}
			?>

        <div class="row justify-content-center">
          <div class="col-lg-5 col-md-12" data-aos="fade-up" data-aos-delay="300">
            <form action="log.php" method="POST" role="form" class="php-email-form">
              <div class="form-group">
                <input type="email" name="email" class="form-control" id="name" placeholder="Username" required>
              </div>
              <div class="form-group">
                <input type="password" class="form-control" name="password" id="email" placeholder="Password" required>
              </div>
              <div class="text-center"><button type="submit" name="submit">Sign In</button></div> <br>
			  <div class="text-center">Don't have an account? <a href="signup.php">Sign Up</a></div>
            </form>
          </div>

        </div>

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