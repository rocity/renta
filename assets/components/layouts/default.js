import Head from 'next/head';
import DefaultHeader from '../includes/headers/default';

import '../../sass/styles.scss';


const DefaultLayout = props => (
  <div>
    <Head>
      <title>Renta Project</title>
    </Head>
    <DefaultHeader></DefaultHeader>
    <div className="container">
      <div className="row">
        <div className="column column-75 column-offset-10">
          {props.children}
        </div>
      </div>
    </div>
  </div>
)

export default DefaultLayout;
