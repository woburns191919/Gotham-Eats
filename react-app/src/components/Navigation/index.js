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
                            <ul>
                                <li>
                                    <ProfileButton user={sessionUser} showMenu={showMenu} />
                                </li>
                            </ul>

                        )}
                        <NavLink exact to="/" className="navbar-logo">
                            <h1>Gotham Eats</h1>
                        </NavLink>
                    </div>


                    <div className="navBar-spacer"></div>


                    <div className="navBar-right">
                        <NavLink to="/cart" className="cart-btn">
                            <i className="fas fa-shopping-cart"></i> Cart
                        </NavLink>
                        {sessionUser ? null : (
                            <>
                                <NavLink to="/login" className="login-btn">
                                    <i className="fas fa-user"></i> Log in
                                </NavLink>
                                <NavLink to="/signup" className="signup-btn">Sign up</NavLink>
                            </>
                        )}
                    </div>
                </div>
            </div>
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
