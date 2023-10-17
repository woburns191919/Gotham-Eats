import React, { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
// import { logout } from "../../store/session";
import * as sessionActions from '../../store/session';
// import { useModal } from '../../context/Modal';
import { useHistory, Link } from "react-router-dom";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserCircle, faBars } from '@fortawesome/free-solid-svg-icons';
import OpenModalMenuItem from './OpenModalMenuItem';


import './Navigation.css'

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const history = useHistory();
  const userInitials = user && `${user.firstName.charAt(0)}${user.lastName.charAt(0)}`;
  const sessionUser = useSelector((state) => state.session.user);
  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener('click', closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu,sessionUser]);

  const closeMenu = () => setShowMenu(false);

  const logout = (e) => {
    e.preventDefault();
    dispatch(sessionActions.logout());
    closeMenu();
    history.push('/');
  };

  // console.log('am i getting user id in here',sessionUser)
  const ulClassName = "profile-dropdown";

  return (
    <>
      <div className="profile-dropdown-container">
        <div className="btn">
          <button className="navigation-btn" aria-label="Main navigation menu" onClick={openMenu}>
            {!user ? (
              <>
                <FontAwesomeIcon icon={faBars} className="menu-icon" />
                <FontAwesomeIcon icon={faUserCircle} className="profile-icon" />
              </>
            ) : (
              <>
                <FontAwesomeIcon icon={faBars} className="menu-icon" />
                <div className="user-initials1">{userInitials.toUpperCase()}</div>
              </>
            )}
          </button>


        </div>
        <div className="menu-drop-down">

          <ul className={ulClassName} ref={ulRef} style={{ display: showMenu ? 'block' : 'none' }}>
            {user ? (
              <>
                <li className="center-menu greeting">Hello, {user.firstName}</li>
                <li className="center-menu email">{user.email}</li>
                <hr />
                <ul className="center-menu">
                  <Link to="/users/show" onClick={closeMenu} style={{ textDecoration: 'none', color: 'black', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <FontAwesomeIcon icon={faUserCircle} style={{ marginRight: '8px' }} />
                    <li className="center-menu center-menu-profile">Your Profile</li>
                  </Link>

                  <li className="center-menu"><button className="Manage-spot-button center-menu1" onClick={(e) => { closeMenu(); history.push(`/owner/restaurants/${sessionUser.id}`) }}>Manage Restaurants</button></li>
                  <li className="center-menu"><button className="Manage-spot-button center-menu1" onClick={(e) => { closeMenu(); history.push('/restaurants/new') }}>Add your Restaurant</button></li>


                  <li><button onClick={logout} className="buttons center-menu center-menu1">Log Out</button></li>
                </ul>
              </>
            ) : (
              <>
                <ul className="center-menu center-menu-login">
                  <OpenModalMenuItem
                    className="center-menu"
                    itemText="Log In"
                    onItemClick={closeMenu}
                    modalComponent={<LoginFormModal />}
                  />
                </ul>
                <ul className="center-menu center-menu-signUp">
                  <OpenModalMenuItem
                    className="center-menu"
                    itemText="Sign Up"
                    onItemClick={closeMenu}
                    modalComponent={<SignupFormModal />}
                  />
                </ul>
                {<Link className="prof-add-res" to='/restaurants/new'>Add your Restaurant</Link>}
              </>
            )}
          </ul>
        </div>
      </div>
    </>
  );
}

export default ProfileButton;


// function ProfileButton({ user }) {
//   const dispatch = useDispatch();
//   const history = useHistory();
//   const { setModalContent, closeModal } = useModal();
//   const [showMenu, setShowMenu] = useState(false);
//   const ulRef = useRef();

//   useEffect(() => {
//     if (!showMenu) return;

//     const closeMenu = (e) => {
//       if (!ulRef.current.contains(e.target)) {
//         setShowMenu(false);
//       }
//     };

//     document.addEventListener("click", closeMenu);

//     return () => document.removeEventListener("click", closeMenu);
//   }, [showMenu]);

//   const handleLogout = (e) => {
//     e.preventDefault();
//     dispatch(logout());
//   };

//   const handleLoginClick = () => {
//     history.push("/login");
//     setModalContent(<LoginFormModal />);
//     closeModal();
//   };

//   const handleSignupClick = () => {
//     history.push("/signup");
//     setModalContent(<SignupFormModal />);
//     closeModal();
//   };

//   const handleProfileClick = () => {
//     if (user) {
//       setShowMenu(!showMenu);
//     } else {
//       setModalContent(
//         <div classname="side-modal">
//           <li><button onClick={handleLoginClick}>Log In</button></li>
//           <li><button onClick={handleSignupClick}>Sign Up</button></li>
//           <Link>Add your restaurant</Link>
//         </div>
//       );
//     }
//   };



//   return (
//     <>
//       <button className="login-signup-menu" onClick={handleProfileClick}>
//         <FontAwesomeIcon icon={faBars} color="white" />
//       </button>
//       <ul className={"profile-dropdown" + (showMenu ? " show" : "")} ref={ulRef}>
//         {user ? (
//           <>
//             <li>{user.username}</li>
//             <li>{user.email}</li>
//             <li>
//             <button onClick={handleLogout} className="buttons center-menu center-menu1">Log Out</button>
//             </li>
//           </>
//         ) : null}
//       </ul>
//     </>
//   );
// }

// export default ProfileButton;
