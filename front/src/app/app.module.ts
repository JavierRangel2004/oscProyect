import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './com/home/home.component';
import { NotFoundComponent } from './com/not-found/not-found.component';
import { NavbarComponent } from './com/navbar/navbar.component';
import { OrganizationsComponent } from './com/organizations/organizations.component';
import { ProjectsComponent } from './com/projects/projects.component';
import { OrganizationDetailsComponent } from './com/organization-details/organization-details.component';
import { ProjectDetailsComponent } from './com/project-details/project-details.component';
import { provideAnimations } from '@angular/platform-browser/animations';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { SigninComponent } from './com/signin/signin.component';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    NotFoundComponent,
    NavbarComponent,
    OrganizationsComponent,
    ProjectsComponent,
    OrganizationDetailsComponent,
    ProjectDetailsComponent,
    SigninComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
