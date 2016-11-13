from flask import url_for

no_subs_page = """<!DOCTYPE HTML>
<!--
	Prologue by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Prologue by HTML5 UP</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="{src1}"></script><![endif]-->
		<link rel="stylesheet" href="{link1}" />
		<!--[if lte IE 8]><link rel="stylesheet" href="{link2}" /><![endif]-->
		<!--[if lte IE 9]><link rel="stylesheet" href="{link3}" /><![endif]-->
	</head>
	<body>

		<!-- Header -->
			<div id="header">

				<div class="top">

					<!-- Logo -->
						<div id="logo">
							<span class="image avatar48"><img src="{src2}" alt="" /></span>
							<h1 id="title">Watson the Lot</h1>
							<p>Parking Helper</p>
						</div>

					<!-- Nav -->
						<nav id="nav">
							<!--

								Prologue's nav expects links in one of two formats:

								1. Hash link (scrolls to a different section within the page)

								   <li><a href="#foobar" id="foobar-link" class="icon fa-whatever-icon-you-want skel-layers-ignoreHref"><span class="label">Foobar</span></a></li>

								2. Standard link (sends the user to another page/site)

								   <li><a href="http://foobar.tld" id="foobar-link" class="icon fa-whatever-icon-you-want"><span class="label">Foobar</span></a></li>

							-->
							<ul>
								<li><a href="#parkinglot" id="top-link" class="skel-layers-ignoreHref"><span class="icon fa-road">Parking Lot</span></a></li>
								<li><a href="#about" id="portfolio-link" class="skel-layers-ignoreHref"><span class="icon fa-question">About Watson the Lot</span></a></li>
								<li><a href="#administration" id="about-link" class="skel-layers-ignoreHref"><span class="icon fa-bar-chart">Administration</span></a></li>
								<li><a href="#futuredev" id="contact-link" class="skel-layers-ignoreHref"><span class="icon fa-lightbulb-o">Future Developement</span></a></li>
							</ul>
						</nav>

				</div>

				<!-- <div class="bottom">

					<!-- Social Icons -->
                    <!--
						<ul class="icons">
							<li><a href="#" class="icon fa-twitter"><span class="label">Twitter</span></a></li>
							<li><a href="#" class="icon fa-facebook"><span class="label">Facebook</span></a></li>
							<li><a href="#" class="icon fa-github"><span class="label">Github</span></a></li>
							<li><a href="#" class="icon fa-dribbble"><span class="label">Dribbble</span></a></li>
							<li><a href="#" class="icon fa-envelope"><span class="label">Email</span></a></li>
						</ul>

				</div> -->

			</div>

		<!-- Main -->
			<div id="main">

				<!-- Intro -->
					<section id="parkinglot" class="one dark cover">
						<div class="container">

							<header>
								<h2 class="alt">Parking Lot</h2>
								<h3 class="alt">{table}</h>
							</header>

							<footer>

							</footer>

						</div>
					</section>

				<!-- Portfolio -->
					<section id="about" class="two">
						<div class="container">

							<header>
								<h2>What is Watson the Lot?</h2>
							</header>

							<p align="left">Watson the Lot uses image recognition to determine the occupancy of a parking lot. It
							then uses this data for a few useful tasks.</p>
							<ul >
								<h3>Features</h3><br>
								<li align="left" style="list-style-type:disc">See how many cars are currently in the parking lot.</li>
								<li align="left" style="list-style-type:disc">Send a notification via text messaging to the user when he/she comes within a certain
								proximity of the parking lot.</li>

							</ul>
							<!--
							<div class="row">
								<div class="4u 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="{src3}" alt="" /></a>
										<header>
											<h3>Ipsum Feugiat</h3>
										</header>
									</article>
									<article class="item">
										<a href="#" class="image fit"><img src="{src4}" alt="" /></a>
										<header>
											<h3>Rhoncus Semper</h3>
										</header>
									</article>
								</div>
								<div class="4u 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="{src5}" alt="" /></a>
										<header>
											<h3>Magna Nullam</h3>
										</header>
									</article>
									<article class="item">
										<a href="#" class="image fit"><img src="{src6}" alt="" /></a>
										<header>
											<h3>Natoque Vitae</h3>
										</header>
									</article>
								</div>
								<div class="4u$ 12u$(mobile)">
									<article class="item">
										<a href="#" class="image fit"><img src="{src7}" alt="" /></a>
										<header>
											<h3>Dolor Penatibus</h3>
										</header>
									</article>
									<article class="item">
										<a href="#" class="image fit"><img src="{src8}" alt="" /></a>
										<header>
											<h3>Orci Convallis</h3>
										</header>
									</article>
								</div>
							</div>
							-->
						</div>
					</section>

				<!-- About Me -->
					<section id="administration" class="three">
						<div class="container">

							<header>
								<h2>About Me</h2>
							</header>

							<a href="#" class="image featured"><img src="{src9}" alt="" /></a>

							<p>Tincidunt eu elit diam magnis pretium accumsan etiam id urna. Ridiculus
							ultricies curae quis et rhoncus velit. Lobortis elementum aliquet nec vitae
							laoreet eget cubilia quam non etiam odio tincidunt montes. Elementum sem
							parturient nulla quam placerat viverra mauris non cum elit tempus ullamcorper
							dolor. Libero rutrum ut lacinia donec curae mus vel quisque sociis nec
							ornare iaculis.</p>

						</div>
					</section>

				<!-- Contact -->
					<section id="futuredev" class="four">
						<div class="container">

							<header>
								<h2>Future Development</h2>
							</header>
							<p>There are several upgrades and additions that can be made to Watson the Lot given time.</p>
							<ul align="left" style="list-style-type:disc">
								<h3>Upgrades</h3>
								<li>Use machine learning to train Watson the Lot to use real snapshots of the parking
								lot. (Also install cameras to make this possible).</li>
								<li>Add user authentication and personalized settings so that others may use the app.</li>
							</ul>
							<ul align="left" style="list-style-type:disc">
								<h3>Additions</h3>
								<li>
									Add visual representations of interesting trends in regards to parking lot occupancy.<br>
									For example: Weather vs. Occupancy, and Time of Day vs. Occupancy.
								</li>
								<li>Use predictive analytics to determine when spots should be opening up in the parking lot.</li>
							</ul>

						</div>
					</section>

			</div>

		<!-- Footer -->
			<div id="footer">

				<!-- Copyright -->
					<ul class="copyright">
						<li>&copy; Untitled. All rights reserved.</li><li>Design: <a href="http://html5up.net">HTML5 UP</a></li>
					</ul>

			</div>

		<!-- Scripts -->
			<script src="{src10}"></script>
			<script src="{src11}"></script>
			<script src="{src12}"></script>
			<script src="{src13}"></script>
			<script src="{src14}"></script>
			<!--[if lte IE 8]><script src="{src15}"></script><![endif]-->
			<script src="{src16}"></script>

	</body>
</html>"""

srcs = {'link1': "assets/css/main.css",
        'link2': "assets/css/ie8.css",
        'link3': "assets/css/ie9.css",
        'src1': "assets/js/ie/html5shiv.js",
        'src2': "images/avatar.jpg",
        'src3': "images/pic02.jpg",
        'src4': "images/pic03.jpg",
        'src5': "images/pic04.jpg",
        'src6': "images/pic05.jpg",
        'src7': "images/pic06.jpg",
        'src8': "images/pic07.jpg",
        'src9': "images/pic08.jpg",
        'src10': "assets/js/jquery.min.js",
        'src11': "assets/js/jquery.scrolly.min.js",
        'src12': "assets/js/jquery.scrollzer.min.js",
        'src13': "assets/js/skel.min.js",
        'src14': "assets/js/util.js",
        'src15': "assets/js/ie/respond.min.js",
        'src16': "assets/js/main.js"}
# subs_page = no_subs_page.format(**({k: v for k, v in srcs.items()}))
# print(subs_page)
