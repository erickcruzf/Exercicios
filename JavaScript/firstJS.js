var balance = 4598.4548798965321524548;
var isActive = true;
var checkBalance = true;

if (checkBalance) {
	if (isActive && balance > 0) {
		console.log("Your balance is $" + balance.toFixed(2) + ".");
	}	
	else if (isActive === false){
		console.log("Your account is no longer active.");
	}
	else if (balance === 0){
		console.log("Your account is empty.");
	}
	else {
		console.log("Your balance is negative. Please contact bank.");
	}
}	
else {
	console.log("Thank you. Have a nice day!");
}

/*https://d17h27t6h515a5.cloudfront.net/topher/2016/November/582cc7b8_atm-check-balance-cropped/atm-check-balance-cropped.jpeg*/