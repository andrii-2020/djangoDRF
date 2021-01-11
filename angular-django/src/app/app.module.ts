import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app.component';
import {HttpClientModule} from '@angular/common/http';
import { OfficesComponent } from './components/offices/offices.component';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import { EmployeesComponent } from './components/employees/employees.component';



@NgModule({
  declarations: [
    AppComponent,
    OfficesComponent,
    EmployeesComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
