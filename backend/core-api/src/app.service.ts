import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getStatus(): { status: string; message: string; timestamp: string } {
    return {
      status: 'online',
      message: 'FitFlow Core API is operational',
      timestamp: new Date().toISOString(),
    };
  }

  getHealth(): { status: string; uptime: number } {
    return {
      status: 'ok',
      uptime: process.uptime(),
    };
  }
}
