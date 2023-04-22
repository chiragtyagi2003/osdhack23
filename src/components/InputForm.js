import { useState, useEffect } from "react";
import { collection, getDocs, addDoc, updateDoc } from "firebase/firestore"
import { db } from "../firebase-config";
import { Link } from 'react-router-dom'

function InputForm() {
    const [names, setName] = useState("");
    const [linkedin, setLinkedin] = useState("");
    const [field, setField] = useState("");

    const usersCollectionRef = collection(db, "yolo");


    // function selection() {
    //     let sel = document.querySelector('#fields');
    //     let op = sel.value;
    //     setField(op);
    // }
    const addUser = async () => {
        let sel = document.querySelector('#fields');
        let op = sel.value;
        setField(op);
        await addDoc(usersCollectionRef, { Name: names, Linkedin: linkedin, Field: field });

    };
    function caller() {
        Selection();
        // opo();
    }
    // function opo() {
    //     setField(this.value) = document.getElementById("#fields").onChange
    // }

    return (
        <>
            <div className=" bg-[rgba(240,165,0,255)] h-screen w-screen fixed">
                {/* <div>
                    <a href="./mainPage ">Research</a>
                </div> */}

                <div className=' bg-white rounded-lg mt-16 p-5 mx-auto h-[550px] w-[550px] '>
                    <p className="font-bold ml-[190px] mt-16  ">Enter your name</p>
                    <input className="w-60  ml-[130px]   border-b-2 border-[rgba(240,165,0,255)]" placeholder='' onChange={(event) => {
                        setName(event.target.value);
                    }} >
                    </input>
                    <p className="font-bold ml-[190px]  mt-5">Enter your LinkedIn</p>
                    <input className='w-60  ml-[130px]   border-b-2 border-[rgba(240,165,0,255)]' placeholder='' onChange={(event) => {
                        setLinkedin(event.target.value);
                    }} >

                    </input>
                    <p className="font-bold ml-[148px] mt-5  ">Enter your Contact Number</p>
                    <input className="w-60  ml-[130px]   border-b-2 border-[rgba(240,165,0,255)]" placeholder='' onChange={(event) => {
                        setName(event.target.value);
                    }} >
                    </input>


                    {/* //FIELD SELECTION MENU */}
                    <div className="w-96 mt-5 ">

                        <p className="font-bold ml-[190px]  ">SELECT YOUR FIELD</p>
                        <select id="fields" class="  ml-[150px] mt-2 w-56 bg-gray-50 border-2 border-[rgba(240,165,0,255)] text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block  p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <option selected> Choose field</option>
                            <option value="AI"  >Artificial Intelligence</option>


                            <option value="BC"> BlockChain</option>

                        </select>
                        <button onClick={addUser} type="Submit" className='rounded border-[rgba(240,165,0,255)] border-2 mt-5 w-[150px] ml-[190px] p-2 hover:bg-[rgba(240,165,0,255)] hover:text-white'>SUBMIT</button>
                    </div>



                </div >
            </div >




        </>
    )
}
export default InputForm
