<?php
session_start();
include('connection.php');

if (isset($_POST['submit']))
{	
$username=$_POST['email']; 
$password=$_POST['password']; 

	if($username=="admin@gmail.com" && $password=="admin")
	{
		$_SESSION['user']='admin';
		header("location:admin/dashboard/dashboard.php");
	}
	else{

		$sel="SELECT * FROM reg WHERE email='$username' and password='$password'";
		$result = mysqli_query($con,$sel) or die(mysql_error());
		$rows = mysqli_num_rows($result);
		$row=mysqli_fetch_array($result);
		
		if($rows==1)
		{	
			$_SESSION['usertype']='user';
			$_SESSION['user']=$row['id'];
			header("location:index.php");
			
		}
		else{
			
			header("location:signin.php?st=fail");
		}
	}
}

?>
 
 



