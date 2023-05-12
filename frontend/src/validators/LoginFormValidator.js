class LoginFormValidator {
  valid(data) {
    let flagFilled = (
      data.username &&
      data.password 
      );

    return flagFilled;
  }
}

export default new LoginFormValidator();