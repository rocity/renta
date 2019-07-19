import DefaultLayout from '../../components/layouts/default';

const SignIn = () => (
  <DefaultLayout>
    <h1>Sign In</h1>
    <form>
      <fieldset>
        <label>Username</label>
        <input type="text" name="username" id="username" />
      </fieldset>
      <fieldset>
        <label>Password</label>
        <input type="password" name="password" id="password"/>
      </fieldset>
    </form>
  </DefaultLayout>
);

export default SignIn;
