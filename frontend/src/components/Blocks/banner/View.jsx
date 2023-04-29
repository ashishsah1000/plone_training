import React from 'react';
import { Container } from 'semantic-ui-react';

const BannerView = (props) => {
  return (
    <div className="full-width" style={{ marginTop: '-30px' }}>
      <div
        style={{
          display: 'flex',
          height: '90vh',
          width: '100vw',
          justifyContent: 'center',
          alignItems: 'center',
        }}
      >
        <div className="banner-overlay">
          <div className="banner-content">
            <h1 className="title">We create Moments</h1>
            <p className="tagline-custom">
              Life is a party, and we're here to help you celebrate!
            </p>
            <button className="button">Learn More</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default BannerView;
