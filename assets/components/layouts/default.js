import Head from 'next/head';
import DefaultHeader from '../includes/headers/default';

import '../../sass/styles.scss';


const DefaultLayout = props => {
  return (
    <div>
      <Head>
        <title>Renta Project</title>
      </Head>
      <div className="container">
        <div className="row">
          <div className="column column-75 column-offset-10">
            {props.children}
          </div>
        </div>
      </div>
    </div>
  )
}

export default DefaultLayout;
