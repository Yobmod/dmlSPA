'use strict';

angular.module('dmlSPA').
    config(function(
		$locationProvider,
		$routeProvider
	){

		$locationProvider.html5Mode({enabled:true})
		$routeProvider
		.when("/blog", {templateURl: 'index.html'})
		.when("/blog/:id", {template: "<blog-list></blog-list>"})
		.when("/blog/:id/:abc", {template: "<h3>post 3</h3>"})

		.when("/contact", {templateURl: 'contact.html'}) //contact page served by flask, should be own app?
		.when("/contact/why", {template: "<h3>why o why</h3>"}) //otherwise all ngRoutes correspond to dmlSPA
		.otherwise({ redirectTo: '/'})




	});
