'use strict';

angular.module('dmlSPA').
    config(function(
		$locationProvider,
		$routeProvider
	){

		$locationProvider.html5Mode({enabled:true})
		$routeProvider
		.when("/blog", {templateURl: 'index.html'})
		.when("/blog/:id", {template: "<h3>post id</h3>"})
		.when("/blog/:id/:abc", {template: "<h3>post 3</h3>"})
		.when("/blog/popp", {template: "<h3>post 4</h3>"})
		.when("/contact", {template: 'templates/contact.html'})
		.otherwise({ redirectTo: '/'})




	});
