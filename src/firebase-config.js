
import { getFirestore } from "@firebase/firestore";
import { initializeApp } from "firebase/app";


const firebaseConfig = {
    apiKey: "AIzaSyCkqkip_ILRSvM8Ni14fp_WBsWTWxUfMfc",
    authDomain: "osdc-fa211.firebaseapp.com",
    projectId: "osdc-fa211",
    storageBucket: "osdc-fa211.appspot.com",
    messagingSenderId: "203358052568",
    appId: "1:203358052568:web:7caa70ac808d3d2a7837ad",
    measurementId: "G-720296C9X7"
};
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);