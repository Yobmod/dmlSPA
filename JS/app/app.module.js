'use strict';

angular.module('dmlSPA',
[	'ngResource',
	'ngRoute',


	'blogList'

], function($interpolateProvider) {	 //camelcase dashes
    // set custom delimiters for angular templates
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
