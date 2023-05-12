class RegistrationFormValidator {
  valid(data) {
    let flagFilled = (
      data.name && 
      data.surname && 
      data.login &&
      data.email &&
      data.surname &&
      data.password && 
      data.rePassword);

    let email_pattern = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/;
    let flagEmail = email_pattern.test(String(data.email).toLowerCase());
    let flagSecurePassword = String(data.password).length >= 2;
    let flagSamePasswords =  (data.password === data.rePassword);

    return flagFilled && flagEmail && flagSamePasswords && flagSecurePassword;
  }
}

export default new RegistrationFormValidator();