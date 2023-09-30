import { useState } from 'react';


const useFormValidation = () => {
    const [validationObj, setValidationObj] = useState({});


    const clearValidationError = (validationField) => {
        setValidationObj((prev) => {
            const newObj = { ...prev };
            delete newObj[validationField];
            return newObj;
        });
    };


    const handleInputChange = (setterFunction, validationField) => (e) => {
        setterFunction(e.target.value);
        clearValidationError(validationField);
    };


    return {
        validationObj,
        handleInputChange,
    };
};


export default useFormValidation;
