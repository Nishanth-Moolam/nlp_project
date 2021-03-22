import { BrowserModule } from '@angular/platform-browser';
import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { HttpClientModule } from '@angular/common/http'
import { CommonModule } from "@angular/common";
import { RouterModule } from '@angular/router';

import { MatToolbarModule } from '@angular/material/toolbar';
import { MatTabsModule }  from '@angular/material/tabs';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ServicesService } from './services.service';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BottomBannerComponent } from './bottom-banner/bottom-banner.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    BottomBannerComponent
  ],
  imports: [
    BrowserModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule, 
    CommonModule, BrowserAnimationsModule,
    MatToolbarModule,
    MatTabsModule
  ],
  exports: [
  ],
  schemas: [ CUSTOM_ELEMENTS_SCHEMA ],
  // put services in providers
  providers: [ServicesService],
  bootstrap: [AppComponent]
})
export class AppModule { }
