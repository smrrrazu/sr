
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
    $scope.products=[
                    {name:'iPhone 5', category:'Mobile', price:5000.25},
                    {name:'Mac book', category:'Laptop', price:9000.99},
                    {name:'Samsung', category:'Mobile', price:3000.25}
                    ];
});
