function [ph,G] = plot_grid_graph(ADJ,COORDS,c)
% function [ph,G] = plot_grid_graph(ADJ,COORDS,c)
% INPUTS:
%   ADJ: NxN adjancency matrix where ADJ(i,j) is the edge cost between i
%   and j'th vertices
%   
%   COORDS: Nx2 vector containing the x and y coordinates of each vertex
%   
%   c: scalar between 0 and 1 which gives the color to use to plot each 
%   vertex 
%
% OUTPUTS:
%   ph: plot handle which can be used later to update the colors.
%   For example, ph.NodeCData(find(OPEN==1)) = 0.33
%   
%   G: graph (MATLAB data structure) based on the given ADJ input

N = size(ADJ,1);
ADJ(isinf(ADJ)) = 0;
G = graph(ADJ);
ph = plot(G); axis equal;
ph.NodeLabel = {};
ph.Marker = 'o';
ph.NodeCData = c*ones(N,1);
ph.MarkerSize = 10;
ph.LineWidth = 1;

ph.XData = COORDS(:,1);
ph.YData = COORDS(:,2);