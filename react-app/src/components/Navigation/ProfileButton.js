import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { useModal } from '../../context/Modal';
import { useHistory } from "react-router-dom";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';

import './Navigation.css'

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const { setModalContent, closeModal } = useModal();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
  };

  const handleLoginClick = () => {
    history.push("/login");
    setModalContent(<LoginFormModal />);
    closeModal();
  };

  const handleSignupClick = () => {
    history.push("/signup");
    setModalContent(<SignupFormModal />);
    closeModal();
  };

  const handleProfileClick = () => {
    if (user) {
      setShowMenu(!showMenu);
    } else {
      setModalContent(
        <div>
          <li><button onClick={handleLoginClick}>Log In</button></li>
          <li><button onClick={handleSignupClick}>Sign Up</button></li>
        </div>
      );
    }
  };

  return (
    <>
      <button className="login-signup-menu" onClick={handleProfileClick}>
        <FontAwesomeIcon icon={faBars} color="white" />
      </button>
      <ul className={"profile-dropdown" + (showMenu ? " show" : "")} ref={ulRef}>
        {user ? (
          <>
            <li>{user.username}</li>
            <li>{user.email}</li>
            <li>
              <button onClick={handleLogout}>Log Out</button>
            </li>
          </>
        ) : null}
      </ul>
    </>
  );
}

export default ProfileButton;
