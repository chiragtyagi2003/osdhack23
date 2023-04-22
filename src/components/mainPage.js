import React from 'react'
import { useState, useEffect } from 'react'
import { getDocs, collection } from 'firebase/firestore'
import { db } from "../firebase-config";
const MainPage = () => {
    const [users, setUsers] = useState([]);

    const usersCollectionRef = collection(db, "yolo");
    useEffect(() => {
        const getUsers = async () => {
            const data = await getDocs(usersCollectionRef);
            console.log(data);
            setUsers(data.docs.map((doc) => ({ ...doc.data(), id: doc.id })))
        }
        getUsers();
    }, []);
    const [filtered, setFiltered] = useState([]);
    function selection() {
        let op;
        const sel = document.querySelector('#fieldMain');
        op = sel.value;


        setFiltered(users.filter(user => {
            return user.Field === op;

        }))


    }

    function changer(co) {
        if (co == 'AI') {
            return true;
        }
        return false;

    }



    return (
        <>
            <div className='h-screen  w-screen bg-indigo-100'>
                <div className=''>
                    {/* OPTIONS FOR SELECTION ON TITLE/ */}
                    <div className="w-72  mx-auto ">

                        <label for="countries" class="block mb-2 ml-16 font-extrabold text-2xl  text-gray-900 dark:text-white">SELECT FIELD</label>
                        <select id="fieldMain" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            <option selected>Select your field of Research</option>
                            <option value="AI">Artificial Intelligence</option>
                            <option value="BC">BlockChain</option>

                        </select>
                        <button onClick={selection} className='ml-16 bg-orange-200 px-2 mt-2 border-2 rounded-md' >Start Your Research</button>

                    </div>

                </div>

                <div className='flex'>
                    <div className='bg-white  h-[600px] w-[300px] ml-5'>
                        <p className='mx-auto ml-20 font-bold'>Related news letters</p>
                        <div></div>
                    </div>
                    {/* INFO BOX */}
                    <div className='bg-white h-[500px] w-[700px] mt-5 mx-auto'></div>


                    {/* EXPERTS BOX */}
                    <div className='bg-white h-[600px] w-[300px] mr-5'>
                        <p className='mx-auto ml-20 font-bold'>Relevant Experts</p>

                        <div className="mt-5 ml-10 space-y-2">
                            {filtered.map((fuser) => {
                                return (

                                    <div key={fuser.Name}>
                                        <ul className=''>
                                            <li className=''> {fuser.Name}</li>
                                            <li className='font-bold'>
                                                {changer(fuser.Field) ? `ARTIFICIAL INTELLIGENCE` : `BLOCKCHAIN`}

                                            </li>
                                            <li className='italic underline' >{fuser.Linkedin}</li>

                                        </ul>
                                    </div>

                                )
                            })}
                        </div >
                    </div>
                </div >



            </div>
        </>

    )

}
export default MainPage
