'use strict';

angular.module('dmlSPA', ['blogList'], function($interpolateProvider) {	 //camelcase dashes
    // set custom delimiters for angular templates
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
