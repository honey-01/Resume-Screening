<?php
session_start();
error_reporting(0);
include("header.php");
include("tables.php");
//include("../header_inner.php");

$del_id=0;
$i=0;
?>
<!-- End Header -->

  <!-- ======= Hero Section ======= -->
<br><br><br><br>

  <main id="main" style="min-height:640px;">

   
   
	<section id="contact" class="contact">
      <div class="container">

        <div class="section-title" data-aos="fade-up">
          <h2>VIEW POST</h2>
        </div>

        <div class="row justify-content-center">

          <div class="col-lg-8 col-md-12" data-aos="fade-up" data-aos-delay="300">
		  <table class='table'>
		  
		  <tr>
		  <th>Name</th>
		  <th>Description</th>
		  <th>Date</th>
		  <th>Apply</th>
		  </tr>
      <?php  
include('connection.php');
$res=mysqli_query($con,"SELECT * FROM jobpost");
$i=1;
				 while($row=mysqli_fetch_array($res))
				{

 ?> 
			<tr>
			<td><?php echo $row['name']; ?></td>
			<td><?php echo $row['description']; ?></td>
			<td><?php echo $row['date']; ?></td>
			<td><a href="fileupload.php?id=<?php echo $row['id'] ?>">Apply</a></td>
			
			
			</tr>
			
			
				 <?php
$i++;
				}
?>
			
          </div>

        </div>
		
	
		
      </div>
    </section> 

  </main><!-- End #main -->

  <!-- ======= Footer ======= -->
  

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="./assets/vendor/purecounter/purecounter.js"></script>
  <script src="./assets/vendor/aos/aos.js"></script>
  <script src="./assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="./assets/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="./assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="./assets/vendor/swiper/swiper-bundle.min.js"></script>

  <!-- Template Main JS File -->
  <script src="./assets/js/main.js"></script>

</body>

</html>