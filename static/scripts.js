;(function(d) {

	'use strict';

	d.addEventListener('keypress', async (e) => {

		const data = {key: e.key};

		const response = await fetch('http://localhost:8080/api/keypress', {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				'Content-Type': 'application/json'
			}
		});
		const text = await response.text();
		console.log(text);
	});

})(document);
