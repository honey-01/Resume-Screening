<?php
//session_start();
include("header.php");
?>

  <!-- ======= Hero Section ======= -->
<br><br><br><br>

  <main id="main" style="min-height:640px;">

   
    <section id="contact" class="contact">
      <div class="container">

        <div class="section-title" data-aos="fade-up">
          <h2>File Upload</h2>
        </div>

        <div class="row justify-content-center">

          <div class="col-lg-5 col-md-12" data-aos="fade-up" data-aos-delay="300">
            <form method="POST"  enctype="multipart/form-data" class="php-email-form">
              
			  <div class="form-group mt-3">
			    <label for="name">File</label>
			    <input type="file" class="form-control" name="image"  placeholder="Name" required autocomplete="off">
			  </div>
			  
              <div class="text-center"><button type="submit" name="submit">Upload</button></div> <br>
            </form>
          </div>

        </div>
<?php
include ("connection.php");
if(isset($_POST['submit']))
{
    $user_id=$_SESSION['user'];
	$jobid=$_REQUEST['id'];
   
if($_FILES['image']['name']){
move_uploaded_file($_FILES['image']['tmp_name'], "uploads/".$_FILES['image']['name']);
$image=$_FILES['image']['name'];
}
    $ins="INSERT INTO `fileupload`( `user_id`, `jobid`, `file`) 
	VALUES ('$user_id','$jobid','$image')";
	//echo $ins;
    if(mysqli_query($con,$ins))
	{
	echo '<script>alert("Succesfully Uploaded!")
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