import React, { useState } from "react";
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }) {
  const sessionUser = useSelector(state => state.session.user);
  const [showMenu, setShowMenu] = useState(false);

  return (
      <>
          <div className="navBar-container">
              <div className="navBar-inner-container">

                  <div className="navBar-left">
                      {isLoaded && (
                       <ul style={{ borderTopStyle: 'solid', borderTopWidth: '12px' }}>
                       <li>
                           <ProfileButton user={sessionUser} showMenu={showMenu} />
                       </li>
                   </ul>

                      )}
                      <NavLink exact to="/" className="navbar-logo">
                          <h1>BringMeFood</h1>
                      </NavLink>
                  </div>


                  <div className="navBar-spacer"></div>


                  <div className="navBar-right">
                      {sessionUser ? null : (
                          <>
                              <NavLink to="/login" className="login-btn">Log in</NavLink>
                              <NavLink to="/signup" className="signup-btn">Sign up</NavLink>
                          </>
                      )}
                  </div>
              </div>
          </div>
          <hr className="line"></hr>
      </>
  );
}


export default Navigation;


// // 	return (
// // 		<ul>
// // 			<li>
// // 				<NavLink exact to="/">Home</NavLink>
// // 			</li>
// // 			{isLoaded && (
// // 				<li>
// // 					<ProfileButton user={sessionUser} />
// // 				</li>
// // 			)}
// // 		</ul>
// // 	);
// // }

// // export default Navigation;
