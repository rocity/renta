import { Component } from 'react';
import Router from 'next/router';
import nextCookie from 'next-cookies';
import cookie from 'js-cookie';

export const login = async ({token}) => {
  cookie.set('token', token, {expires: 1});
  Router.push('/profile');
};

export const signout = () => {
  cookie.remove('token');
  window.localStorage.setItem('signout', Date.now())
  Router.push('/signin');
};

const getDisplayName = Component => Component.getDisplayName || Component.name || 'Component'

export const withAuthSync = WrappedComponent => (
  class extends Component {
    static displayName = `withAuthSync(${getDisplayName(WrappedComponent)})`;

    static async getInitialProps(ctx) {
      const token = auth(ctx);

      const componentProps =
        WrappedComponent.getInitialProps &&
        (await WrappedComponent.getInitialProps(ctx));

      return { ...componentProps, token };
    }

    constructor(props) {
      super(props);
      this.syncSignout = this.syncSignout.bind(this);
    }

    componentDidMount() {
      window.addEventListener('storage', this.syncSignout);
    }

    componentWillUnmount() {
      window.removeEventListener('storage', this.syncSignout);
      window.localStorage.removeItem('signout');
    }

    syncSignout(e) {
      if (e.key === 'signout') {
        Router.push('/signin');
      }
    }

    render() {
      return <WrappedComponent {...this.props} />
    }
  }
)

export const auth = ctx => {
  // Server side auth check
  const {token} = nextCookie(ctx);

  if (ctx.req && !token) {
    // Request is present but token isn't means the user is not logged in.
    ctx.res.writeHead(302, {Location: '/signin'});
    ctx.res.end();
    return;
  }

  if (!token) {
    Router.push('/signin');
  }

  return token;
}
