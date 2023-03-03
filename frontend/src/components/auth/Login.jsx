import {  useNavigate } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { login } from "../../actions/userActions"


// error


const ErrorMessage = () => {
  return (
    <div
      role="alert"
    >
      <strong>Holy smokes!</strong>
      <span ></span>
      <span >
          <title>Close</title>
      </span>
    </div>
  );
};

// loading

const Loading = () => {
  return (
    <div >
  <div role="status">
    <div className="status-text"></div>
  </div>
</div>
  );
};


// login


export const Login = ({ history }) => {

  const navigate = useNavigate()

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();

  const userLogin = useSelector((state) => state.userLogin);

  const { loading, error, userInfo} = userLogin

  useEffect(() => {
    if (userInfo) {
      navigate("/dashboard")
    } 
  }, [navigate, userInfo])
  

  const submitHandler = async (e) => {
    e.preventDefault();
    dispatch(login(email, password))
  };


  return (
    <>
      <div>Login</div>
      {error && <ErrorMessage />}
      {loading && <Loading />}
      <form
        onSubmit={submitHandler}
        action="/dashboard">
        
        <label>Email</label>
        <input type={"email"} placeholder="enter email" onChange={(e) => setEmail(e.target.value)}/>
        <label>Password</label>
        <input type={"password"} placeholder="enter password" onChange={(e) => setPassword(e.target.value)}/>
        <button
              type="submit"
            >
              Sign in
            </button>
      </form>
    </>
  )
}
