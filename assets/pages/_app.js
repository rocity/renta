import React from 'react';
import App, { Container } from 'next/app';
import nextCookie from 'next-cookies';

import DefaultLayout from '../components/layouts/default';
import DefaultHeader from '../components/includes/headers/default';


class RentaApp extends App {
  static async getInitialProps({Component, router, ctx}) {
    const { token } = nextCookie(ctx);
    let pageProps = {};

    if (Component.getInitialProps) {
      pageProps = await Component.getInitialProps(ctx);
    }

    pageProps['isAuthed'] = !!token;

    return { pageProps };
  }

  render() {
    const {Component, pageProps} = this.props;

    return (
      <Container>
        <DefaultLayout {...pageProps}>
          <DefaultHeader {...pageProps}></DefaultHeader>
          <Component {...pageProps} />
        </DefaultLayout>
      </Container>
    )
  }
}

export default RentaApp;
