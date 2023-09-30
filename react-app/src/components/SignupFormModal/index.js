import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [firstName, setFirstName] = useState("");
	const [lastName, setLastName] = useState("");
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [streetAddress, setStreetAddress] = useState("");
	const [city, setCity] = useState("");
	const [state, setState] = useState("");
	const [postalCode, setPostalCode] = useState("");
	const [country, setCountry] = useState("");
	const [phone, setPhone] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();


	const handleModalClose = () => {
		setFirstName("");
		setLastName("");
		setEmail("");
		setUsername("");
		setStreetAddress("");
		setCity("");
		setState("");
		setPostalCode("");
		setCountry("");
		setPhone("");
		setPassword("");
		setConfirmPassword("");
		setErrors({});
		closeModal();
	};

	const isSignupDisabled =
		!firstName ||
		!lastName ||
		!email ||
		username.length < 4 ||
		!streetAddress ||
		!city ||
		!state ||
		!postalCode ||
		!country ||
		!phone ||
		password.length < 6 ||
		!confirmPassword;


	const handleSubmit = async (e) => {
		e.preventDefault();
		let newErrors = {};

		if (!firstName) newErrors.firstName = "First name is required";
		if (!lastName) newErrors.lastName = "Last name is required";
		if (!email.includes("@")) newErrors.email = "Must be a valid email";
		if (username.length <= 4) newErrors.username = "username must be greater than four characters";
		if (!streetAddress) newErrors.streetAddress = "Street Address is required";
		if (!/^\d+$/.test(postalCode)) newErrors.postalCode = "Zip Code must be numbers";
		if (!/^\d+$/.test(phone)) newErrors.phone = "Phone must be a number";
		if (password.length < 6) newErrors.password = "Password must be at least six characters";
		if (password !== confirmPassword) newErrors.confirmPassword = "Confirm Password field must be the same as the Password field";
		if (city !== "Gotham") newErrors.city = "City must be Gotham";
		if (state !== "New York") newErrors.state = "State must be New York";
		if (country !== "United States") newErrors.country = "Country must be United States";

		if (Object.keys(newErrors).length === 0) {
			const data = await dispatch(signUp(firstName, lastName, username, password, email, streetAddress, city, state, postalCode, country, phone,));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors(newErrors);
		}
	};


	return (
		<div>
			<h1 className="sign">Sign Up</h1>
			<form className="modal-content" onSubmit={handleSubmit}>
				<label>
					First Name
					{errors.firstName && <p className="error">{errors.firstName}</p>}
					<input
						type="text"
						value={firstName}
						onChange={(e) => setFirstName(e.target.value)}
						required
					/>
				</label>
				<label>
					Last Name
					{errors.lastName && <p className="error">{errors.lastName}</p>}
					<input
						type="text"
						value={lastName}
						onChange={(e) => setLastName(e.target.value)}
						required
					/>
				</label>
				<label>
					Email
					{errors.email && <p className="error">{errors.email}</p>}
					<input
						type="text"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</label>
				<label>
					username
					{errors.username && <p className="error">{errors.username}</p>}
					<input
						type="text"
						value={username}
						onChange={(e) => setUsername(e.target.value)}
						required
					/>
				</label>
				<label>
					Address
					{errors.streetAddress && <p className="error">{errors.streetAddress}</p>}
					<input
						type="text"
						value={streetAddress}
						onChange={(e) => setStreetAddress(e.target.value)}
						required
					/>
				</label>
				<label>
					City
					{errors.city && <p className="error">{errors.city}</p>}
					<input
						type="text"
						value={city}
						onChange={(e) => setCity(e.target.value)}
						required
					/>
				</label>
				<label>
					State
					{errors.state && <p className="error">{errors.state}</p>}
					<input
						type="text"
						value={state}
						onChange={(e) => setState(e.target.value)}
						required
					/>
				</label>
				<label>
					Zip Code
					{errors.postalCode && <p className="error">{errors.postalCode}</p>}
					<input
						type="text"
						value={postalCode}
						onChange={(e) => setPostalCode(e.target.value)}
						required
					/>
				</label>
				<label>
					Country
					{errors.country && <p className="error">{errors.country}</p>}
					<input
						type="text"
						value={country}
						onChange={(e) => setCountry(e.target.value)}
						required
					/>
				</label>
				<label>
					Phone
					{errors.phone && <p className="error">{errors.phone}</p>}
					<input
						type="text"
						value={phone}
						onChange={(e) => setPhone(e.target.value)}
						required
					/>
				</label>
				<label>
					Password
					{errors.password && <p className="error">{errors.password}</p>}
					<input
						type="text"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</label>
				<label>
					Confirm Password
					{errors.confirmPassword && <p className="error">{errors.confirmPassword}</p>}
					<input
						type="text"
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
					/>
				</label>
				<button type="submit">Sign Up</button>
			</form>
		</div>
	);
}

export default SignupFormModal;
