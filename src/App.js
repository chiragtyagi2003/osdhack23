// Importing modules
import React, { useState, useEffect } from "react";


function App() {
	// usestate for setting a javascript
	// object for storing and using data
	const [data, setdata] = useState({
		name: "",
		age: 0,
		date: "",
		programming: "",
	});

	// Using useEffect for single rendering
	useEffect(() => {
		// Using fetch to fetch the api from
		// flask server it will be redirected to proxy
		fetch("/data").then((res) =>
			res.json().then((data) => {
				// Setting a data from api
				setdata({
					name: data.Name,
					age: data.Age,
					date: data.Date,
					programming: data.programming,
				});
			})
		);
	}, []);

	return (
		<div className="App">
			<header className="App-header">
				<h1>React and flask</h1>
				{/* Calling a data from setdata for showing */}
				<p>{data.name}</p>
				<p>{data.age}</p>
				<p>{data.date}</p>
				<p>{data.programming}</p>

			</header>
		</div>
	);
}

export default App;













// import Inputform from './components/InputForm'
// import Main from './components/mainPage'
// import Home from '../src/components/home'
// import ReactDOM from "react-dom/client";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import MainPage from './components/mainPage';
// import Plag from './components/plag';
// function App() {
  
//   return (
//     <div className="App">

//       <BrowserRouter>
//         <Routes>
//           <Route path="/components/InputForm" element={<Inputform />} />
//           <Route path="/" element={<Home />} />
//           <Route path="/components/mainPage" element={<MainPage />} />
//           <Route path="/components/plag" element={<Plag />} />

//         </Routes>
//       </BrowserRouter>
//     </div>
//   );
// }

// export default App;
